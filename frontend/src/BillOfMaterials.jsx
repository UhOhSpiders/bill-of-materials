import React from "react";

const BillOfMaterials = ({ data }) => {
  const products = data.map((product, index) => {
    return (
      <div>
        <h2 key={index}>{product.name}</h2>
        {product.components.map((component) => {
          return (
            <>
              <h3>
                {component.name} {component.cost} {component.stock_level}
              </h3>
              {component.sub_components.map((subcomponent) => {
                return <><p>{subcomponent.name}</p></>
              })}
            </>
          );
        })}
      </div>
    );
  });

  return (
    <>
      <div>{products}</div>
    </>
  );
};

export default BillOfMaterials;
