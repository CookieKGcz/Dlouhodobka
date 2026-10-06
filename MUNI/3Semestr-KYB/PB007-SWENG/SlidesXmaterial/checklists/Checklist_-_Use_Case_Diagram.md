# Use Case Diagram


## Syntax


- [ ] All use cases are encapsulated inside the system boundary
- [ ] All «include»/«extend» relationship arrows are dashed
- [ ] «include» relationships have arrows going from the main activity to the sub-activity
- [ ] «extend» relationships have arrows going from the sub-activity to the main activity
- [ ] Main use cases of «extend» relationships have appropriately-named extension points


## Best practices


- [ ] The system is named
- [ ] Only one system is modelled
- [ ] Time-dependent activities are performed by a special «Time» actor
        - [ ] The information about the time is denoted on the relationship or via the Actor’s naming
- [ ] «extend»ed use cases are complete without their extensions


## Semantics


- [ ] One-directional interaction between an actor and a use case is denoted by an arrow (→) 
- [ ] All activities are performable _in the system_
- [ ] Actor generalisation signifies an ‘is-a’ relationship -- no  activities are propagated into inappropriate contexts
- [ ] Use case names include verbs (and represent actions)
- [ ] External system actors are denoted by a «System» tag


## Style


- [ ] The diagram looks tidy and is readable
- [ ] Naming conventions are consistent
- [ ] Lines do not cross each other if it can be avoided


## Recommendations


- [ ] «include», «extend» and generalisation relationships are only used if they simplify the diagram (or unless explicitly asked to be used as a part of a task)
- [ ] All actors in the assignment are captured




# Textual specification


- [ ] The specification uses the shared template
    - [ ] All the sections are filled in
- [ ] All lines follow the `«id» «actor» «action»` syntax
- [ ] Instead of using the conjunction ‘and’, sentences are split into two separate steps
- [ ] Key words are written in capital letters
- [ ] Bodies of nested flows are indented
- [ ] The post-condition is met in all branches of the main flow
- [ ] Lines are numbered
    - [ ] The numbering of indented lines follows the indentation (2.2)
- [ ] All possible errors are listed in the alternate flow
    - [ ] If possible, they show on what line in the main flow the error can occur
- [ ] The main flow does not model errors (i.e. follows the ‘sunny road’ scenario)
- [ ] Branch conditions are on separate lines from the bodies