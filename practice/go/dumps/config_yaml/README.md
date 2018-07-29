1. while reading in yaml file, order doesn't matter
2. tags in struct `yaml:"cRenamed"` are used to specify renaming while marshalling
3. random comments in between yaml don't matter
4. exact string case sensistibity automatically handled
5. struct vars should public
6. nested struct parent field can't have a different name (case insensitive is ok).
7. conflict resolution while unmarshalling https://godoc.org/gopkg.in/yaml.v2#example-Unmarshal--Embedded
8. 