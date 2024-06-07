export const getNestedCosts = (assembly) => {
  let nestedCosts = { [assembly.name]: 0 };
  assembly.subassemblies.map((subassembly) => {
    subassembly.components.map((component) => {
        nestedCosts[assembly.name] += component.cost
        nestedCosts[subassembly.name] = nestedCosts[subassembly.name] || 0
        nestedCosts[subassembly.name] += component.cost
    });
  });
  return nestedCosts;
};
