## Basic concepts
- Indexing mechanisms used to speed up access to desired data.
	- author catalog in library
- Search key - id
- An index file consists of records (called index entries) of the form
	- search-key --- pointer
- Two basic kinds of indices:
	- **Ordered indices**: search keys are stored in sorted order
	- **Hash indices**: search keys are distributed uniformly across “buckets” using a “hash function”.
## Ordered Indices
- In an ordered index, index entries are stored sorted on the search key value
- **Primary index**:
	- assume a sequential file, the index whose search key specifies the sequential order of records in the file.
		- Also called **clustering index**
		- The search key of a primary index is usually but not necessarily the primary key.
- **Secondary index**:
	- an index whose search key specifies an order different from the sequential order of records in the file.
		- Also called **non-clustering index**
## Dense Index Files (primary index)
- Dense index
	- Index record appears for every search-key value in the file.
- E.g. index on ID attr. of instructor(id, name, dept_name, salary)
- ![[Pasted image 20251209171753.png | 500]]
- Dense index on dept_name, with instructor file sorted on dept_name
- ![[Pasted image 20251209172008.png | 500]]
## Sparse Index Files
- Sparse Index
	- Contains index records for only some search-key values
	- Applicable when records are sequentially ordered on search-key
- ![[Pasted image 20251209172059.png | 520]]

- Compared to dense indices:
	- Less space and less maintenance overhead for insertions and deletions.
	- Generally slower than dense index for locating records.
- **Good tradeoff**:
	- Sparse index with an index entry for every block in file, corresponding to least search-key value in the block.
	- ![[Pasted image 20251209172209.png | 250]]
## Secondary Indices
xxx https://is.muni.cz/auth/el/fi/podzim2025/PB168/um/slides08-indexing-hashing.pdf?predmet=1654908
## Multilevel Index
- If an index does not fit in memory, access becomes expensive.
- Solution: treat the index kept on disk as a sequential file and construct a sparse index on it.
	- outer index – a sparse index of the original index
	- inner index – the original index file
- ![[Pasted image 20251209172523.png | 300]]
## B+ - Tree Index Files
- B+tree file organization is an alternative to indexed-sequential files.

- Disadvantage of indexed-sequential files
	- Performance degrades as file grows, since many overflow blocks get created. 
	- Periodic reorganization of entire file is required.
- Advantage of B+tree files:
	- Automatically reorganizes itself with small, local, changes, in the face of insertions and deletions.
	- Reorganization of entire file is not required to maintain performance.
- (Minor) disadvantage of B+trees:
	- Extra insertion and deletion overhead, space overhead
- ![[Pasted image 20251209173012.png | 550]]
### B+ Tree Index
- A B+ -tree is a rooted tree satisfying the following properties:
	- All paths from root to leaf are of the same length
	- Each node that is not a root or a leaf has between n/2 and n children.
	- A leaf node has between (n–1)/2 and n–1 values
### B+ Tree Node Structure
- ![[Pasted image 20251209173449.png | 400]]
- Ki are values of the search key
- Pi are pointers to children (for non-leaf nodes) or pointers to records or buckets of records (for leaf nodes).

- The search-key values in a node are ordered!
.
.
.
.
.
.
## Hashing
- In a hash file organization, we obtain the address of a record directly from its search-key value using a hash function
	- Address is typically a bucket – a unit of storage containing one or more records
		- A bucket corresponds to a disk block
- Hash function h
	- a function from the set of all search-key values K to the set of all bucket addresses B
	- used to locate records for access, insertion as well as deletion
- Records with different search-key values may be mapped to the same bucket
	- thus entire bucket has to be searched sequentially to locate a record

- ![[Pasted image 20251209174843.png | 500]]
## Example of Hash File Organization
- Hash function on dept_name can be defined as:
	- The binary representation of the i-th character in the alphabet is assumed to be the integer i
	- The hash function returns the sum of the binary representations of all the characters modulo 8
		- i.e., there are 8 buckets.
- ![[Pasted image 20251209175251.png | 400]]
## Handling of bucket overflows
- Collision occurs when two different search-key values are hashed to the same address (bucket)
- Bucket overflow can occur because of
	- Insufficient bucket size
	- Skew in distribution of records.
- Although the probability of bucket overflow can be reduced, it cannot be eliminated; it is handled by using
	- **Overflow buckets**
	- **Collision function**
### Overflow chaining
- the overflow buckets of a given bucket are chained together in a linked list.
	- This scheme is called closed hashing.
		- ![[Pasted image 20251209175522.png | 300]]
bim bim bim
## Dynamic Hashing

bim bim bim

## Index Definition in SQL
- Create an index
	- ![[Pasted image 20251209175747.png | 300]]
- Drop an index
	- ![[Pasted image 20251209175805.png| 200]]
