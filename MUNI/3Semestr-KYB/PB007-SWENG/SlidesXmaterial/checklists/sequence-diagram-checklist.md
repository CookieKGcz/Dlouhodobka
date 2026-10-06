# Sequence Diagram

## Syntax
- [ ] Each message is numbered correctly
- [ ] Create message and return message lines are dashed and have a line arrow
- [ ] Fragments are tidy and self-contained – they do not include fragments or messages that come out of them
- [ ] Every variable used is either defined before its use or is a concrete value from the actor
- [ ] Fragment conditions are valid boolean expressions in square brackets (‘[…]’)
- [ ]  «create» messages are used for calling the constructor
- [ ]  Recursive calls create nested activations
- [ ] There are no nested function calls (foo(bar())

## Semantics
- [ ] The diagram models only one concrete use-case
- [ ] The actor does not include logic that should be a part of the system
- [ ] Every class instance that is not a singleton (e.g. manager/services classes) are  named
- [ ] Correct operators are used for correct use cases – alt (not opt) for if/else, break (not opt) for stopping a loop
- [ ] Activations are connected if nearby messages are related

## Consistency
- [ ] The actor is present in the use case diagram
- [ ] Each class communicates only with classes it has access to, according to the class diagram
- [ ] It also does not violate attribute/method visibilities
- [ ] Method signatures and return types are consistent with the class diagram

## Recommendations
- [ ] Error handling is done using an OPT fragment
- [ ] Use a different colour for managers