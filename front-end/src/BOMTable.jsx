import React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { getNestedCosts } from "../utilities/getNestedCosts";

const BOMTable = ({ data }) => {
  
  const checkTrue = (arr) => arr.every(obj => obj.complete === true)

  const rows = data.map((assembly, index) => {
    let nestedCosts = getNestedCosts(assembly)
    return (
      <TableBody>
      <TableRow
        key={index}
        sx={{ "&:last-child td, &:last-child th": { border: 1 } }}
        style={{backgroundColor:"red"}}
      >
        <TableCell>{assembly.name}</TableCell>
        <TableCell>{assembly.stock_level}</TableCell>
        <TableCell>total {nestedCosts[assembly.name]}</TableCell>
        <TableCell>assembly</TableCell>
        <TableCell>{checkTrue(assembly.subassemblies)?<>complete</>:<>incomplete</>}</TableCell>
        </TableRow>
        {assembly.subassemblies.map((subassembly, index) => {
          return (
            <>
            <TableRow
            key={index}
            style={{backgroundColor:"grey"}}
            >
              <TableCell
              style={{paddingLeft:50}}
              >{subassembly.name}</TableCell>
              <TableCell>{subassembly.stock_level}</TableCell>
              <TableCell>{nestedCosts[subassembly.name]}</TableCell>
              <TableCell>subassembly</TableCell>
              <TableCell>{subassembly.complete?<>complete</>:<>incomplete</>}</TableCell>
            </TableRow>
              {subassembly.components.map((component) => {
                return (
                  <TableRow>
                  <TableCell
                  style={{paddingLeft:80}}
                  >{component.name}</TableCell>
                  <TableCell>{component.stock_level}</TableCell>
                  <TableCell>{component.cost}</TableCell>
                  <TableCell>component</TableCell>
                </TableRow>
                );
              })}
            </>
          );
        })}
      </TableBody>
    );
  });

  return (
    <>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }}>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Stock Level</TableCell>
              <TableCell>Cost</TableCell>
              <TableCell>Category</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          
            {rows}
          
        </Table>
      </TableContainer>
    </>
  );
};

export default BOMTable;
