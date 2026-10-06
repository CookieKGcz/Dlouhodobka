# Activity diagram

## Syntax
- [ ] The diagram starts with an initial node and ends with a final node
- [ ] All guard conditions are surrounded by square brackets (‘[…]’)
- [ ] Flow final nodes are used for ending one parallel run 
- [ ] Final nodes are used for ending the entire use case

## Best practices
- [ ] Exactly one control flow enters and exits each action
- [ ] Fork nodes are used when parallel flows are needed
- [ ] Each decision node control flow ends in a merge node
- [ ] Each fork control flow ends in a join node
- [ ] Actions symbolise concepts (Show search results), not direct GUI (User clicks on a button) or low-level actions (e.g. saving to specific database)
- [ ] Decision nodes are not used as merge nodes
- [ ] Conditions in decision nodes are not actions

## Semantics
- [ ] The diagram models a specific use-case (or a combination of related use cases (e.g. via include/extend))
- [ ] Actions are atomic within the modelled context
- [ ] Decision node guard conditions cover all possible options, but no option can have multiple possible guards
- [ ] Every action node has a verb
- [ ] Base use cases and included/extending use cases are separated to their own swimlanes
- [ ] There is a decision node in place of an extension point. One option leads to the swimlane of the extending use case, second option remains in the swimlane of the base use case

## Style
- [ ] Naming conventions are consistent

## Recommendations
- [ ] Swimlanes are not used unless they make the diagram clearer or for includes/extends
- [ ] Input forms are a good use case for trying out forks

## Consistency
- [ ] The modelled use case is present in the use case diagram
- [ ] The includes/extends of the modelled use case are consistent between the activity and use case diagram