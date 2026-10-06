# State Diagram

## Creation
- [ ] The diagram models the lifecycle of exactly one object in the system
    - [ ] The object has a non-trivial lifecycle
- [ ] All meaningful states of the object have been identified
    - [ ] Each state describes a unique combination of attributes
- [ ] The first transition represents the constructor call
- [ ] The object is not deleted if it is still used in the system

## Verification
- [ ] Transitions are not described with natural language
- [ ] Call and change events only use operations and attributes from the respective class
    - [ ] Change events do not use attributes of different objects
- [ ] All used operations and attributes are present in the design class diagram
- [ ] Entry/exit events make sense every time they are invoked
