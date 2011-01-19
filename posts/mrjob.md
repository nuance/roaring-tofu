title: Oh No MRJob!

My first tech note is on a project near-and-dear to my heart, Yelp's MRJob library.

A Little Background
===================

I implemented the first version of MRJob after spending some time trying to coax hadoop streaming frameworks to do what I expected. Most existing python MR frameworks, at that point in time, were focused on single step, ad-hoc jobs. I wanted something that could easily handle 5 or more map/reduce pairs and hid all the messy details of hadoop streaming from the end-user.

I also considered [Pig][pig] and [Hive][hive]. Pig looked pretty cool, but only worked with csv input, which wasn't an acceptable limitation. Hive was also interesting, and the idea of using near-SQL was appealing, but the need to invest a large amount of resources in building tables Hive could query was a dealbreaker. At that point in time, it wasn't clear what restrictions we could place on the data in hadoop, and hive required rigid schemas to be constructed. Another big issue, at that time, was that all our logs were stored in pickle, a native python serialization format, which was not easily accessible from anything but python.

Hadoop / MapReduce (the beautiful bits)
=======================================

> MapReduce is a programming model and an associated implementation for processing and generating large data sets. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key.

[Dean, Jeffrey & Ghemawat, Sanjay (2004). "MapReduce: Simplified Data Processing on Large Clusters"][mrpaper]

At a high-level, any MapReduce / Hadoop job is constructed from 2 base elements: mappers & reducers.

A job takes, as an input, a set of chunks, each of which is just a file. The job proceeds to execute the first mapper over every line in every chunk, possibly executing multiple simultaneous mappers. Each of these mappers writes out key-value pairs. These key-value pairs are sorted and grouped by key, then split apart into chunks (with all the values for a specific key in only one chunk). Reducers are called on each key and all it's values, and, like mappers, are given each line of each chunk. These can also be run simultaneously.

At a very high level, this is a simple unix pipeline, like:

    #!bash
    MAPPER='grep food'
    REDUCER='uniq -c'
    cat input.txt | $(MAPPER) | sort | $(REDUCER)

The real power from this comes from 2 sources:

1. **Map-Reduce tasks are parallelizable** - algorithms built as map/reduce pairs are trivial to run in parallel. Just increase the number of mappers and reducers, and your algorithm is running in parallel. In unix land, think `xargs -P`.

2. **Map-Reduce tasks are composable** - map/reduce pairs can be chained together, so that the output of one reduce step feeds into the next map step. Once you've integrated hadoop / map-reduce into your work cycle, you'll find yourself doing things like 'find all log lines matching some criteria, then group them on 2 independent attributes.' You can easily split this into three distinct components ('find all matching log lines,' 'group on attribute 1,' 'group on attribute 2'), which can each be independent map-reduce pairs. In practice you can often collapse operations into single steps, but it's often easier to reason about them independently.

Hadoop Streaming (the messy bits)
=================================

At a high level, map-reduce is pretty simple. You define your mapper and reducer and the system takes care of distributing your work and any intermediate data.

How it works
------------

Hadoop invokes your process, writes to stdin, reads from stdout/stderr.

The Hadoop Streaming protocol
-----------------------------

[Apache documentation][hadoop streaming docs]

1. **Foobar**

[mrpaper]: http://labs.google.com/papers/mapreduce.html
[pig]: http://pig.apache.org/
[hive]: http://hive.apache.org/
[hadoop streaming docs]: http://hadoop.apache.org/mapreduce/docs/r0.21.0/streaming.html#More+Usage+Examples