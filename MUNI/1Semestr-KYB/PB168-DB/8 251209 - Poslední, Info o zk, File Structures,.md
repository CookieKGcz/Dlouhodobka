## Classification of Physical Storage Media
- Speed of access
- Cost per unit of data
- Reliability
- Can differ:
	- Volatile storage: loses contents when power off
	- Non-volatile storage: Contents persists

## Phys. St.Me.
- Cache - fastest and most costly form of storage; volatile; managed by the computer system hardware
- Main memory:
	- fast access
	- generally too small to store the entire database
	- Volatile
- Flash memory:
	- Data survives power failure
	- Data can be written at a location only once, but location can be erased and written to again
	- Writes are slow
	- USB, SSD, phone mem
- Magnetic-disk
	- read/write magnetically
	- Much slower access
- Optical storage
	- Non-volatile
	- data read optically from spinning disk using laser
	- DVD (in GB)
	- Blu-ray (in GB)
- Tape storage

## Storage Hierarchy
- Primary storage
	- fastest/volitale (cache, main memory)
- Secondary storage
	- non-volatile, moderestly fast (also called on-line storage)(flash, magnetic disks)
- Tertiary storage
	- non-vol., slow access, (off-line storage)(magnetic tape, optical storage)
## Performance Measures of Disks
- Access time - the time it takes from when a read or write request is issued to when data transfer begins
	- Seek time - time it takes to reposition the arm over the correct track
	- Rotational latency - time it takes for the sector to be accessed to appear under the head
		- 4 to 11 milliseconds on typical disks (5400 to 15000 rpm)
- Data-transfer rate - the rate at which data can be retrieved from or stored to the disk
	- 25 to 200 MB per second max rate
## Optimization of Disk-Block Access
- Block - a contiguous sequence of sectors from a single track
	- data is transferred between disk and main memory in blocks
	- sizes range from one sector (e.g., 512 bytes) to several sectors (e.g., 4 kilobytes)
- File organization - optimize block access time by organizing the blocks to correspond to how data will be accessed
	- File systems may get fragmented over time
## File Organization
- The database is a collection of relations
	- Relations are stored as individual files.
	- Each file is a sequence of records.
	- A record is a sequence of fields/attributes.
	- ![[Pasted image 20251209164335.png | 400]]
		- Blok ~4KB
### Fixed-Length Records
- Simple approach:
	- Store record i starting from byte n * (i – 1)
		- where n is the size of each record.
	- Record access is simple, but records may cross blocks
		- Solution: do not allow records to cross block boundaries
- Deletion of record i
	1. move records i + 1, . . ., n to i, . . . , n – 1
	2. move record n to i
	3. do not move records, but link all free records on a free list

### Varieble-Length Records
- Variable-length records are common in database systems:
	- Attributes of variable-length type, e.g. strings (varchar)
- Solution:
	- Attributes are stored in order
	- Variable-length attributes represented by fixed size (offset, length)
		- actual data stored after all fixed length attributes (at address of offset)
	- Null values represented by null-value bitmap
- Relation: instructor(id, name, dept_name)
- ![[Pasted image 20251209165120.png | 500]]
#### Slotted Page Structure
- Header contains:
	- number of record entries
	- end of free space in the block
	- location and size of each record
- Records stored from the end of the block

- Record updates
	- Record can be moved around within a page
		- to keep all records contiguous with no empty space between them
		- Only entry in the header must be updated
- ![[Pasted image 20251209165337.png | 400]]
## Organization of Records in Files
- File
	- is usually divided into blocks (atomic size of DB I/O operations)
- Type of file organization:
	- Heap – a record can be placed anywhere in the file where there is space (i.e., in any block, where is a room)
	- Sequential – store records one after the other and in a sequential order, based on the value of the search key of each record
	- Hash – a hash function computed on some attribute of each record; the result specifies in which block of the file the record should be placed
### Sequential File Organization
- Suitable for applications that require sequential processing of the entire file
- The records in the file are ordered by a search-key
	- id
- ![[Pasted image 20251209165736.png | 300]]
#### Sequential File Organization: Updates
- Deletion – use pointer chains
- Insertion – locate the position where the record is to be inserted
	- if there is free space insert there
	- if no free space, insert the record in an overflow block
	- in either case, pointer chain must be updated
- Need to reorganize the file from time to time
- ![[Pasted image 20251209165844.png | 300]]
## Data Dict. Storage