import React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { getNestedCosts } from "../utilities/getNestedCosts";
import { MdSubdirectoryArrowRight } from "react-icons/md";

const BOMTable = ({ data }) => {
  
  const checkChildrenComplete = (arr) => arr.every(obj => obj.complete === true)

  const rows = data.map((assembly, index) => {
    let nestedCosts = getNestedCosts(assembly)
    return (
      <TableBody>
      <TableRow
        key={index}
        sx={{ "&:last-child td, &:last-child th": { border: 1 } }}
        style={{ backgroundColor: checkChildrenComplete(assembly.subassemblies) ? "darkseagreen" : "darkorange" }}
      >
        <TableCell>{assembly.name}</TableCell>
        <TableCell></TableCell>
        <TableCell>£{nestedCosts[assembly.name]}</TableCell>
        <TableCell>assembly</TableCell>
        <TableCell>{checkChildrenComplete(assembly.subassemblies)?<>complete</>:<>incomplete</>}</TableCell>
        </TableRow>
        {assembly.subassemblies.map((subassembly, index) => {
          return (
            <>
            <TableRow
            key={index}
            style={{ backgroundColor: subassembly.complete ? "darkseagreen" : "khaki" }}
            >
              <TableCell
              style={{paddingLeft:50}}
              ><MdSubdirectoryArrowRight/>{subassembly.name}</TableCell>
              <TableCell>{subassembly.stock_level}</TableCell>
              <TableCell>£{nestedCosts[subassembly.name]}</TableCell>
              <TableCell>subassembly</TableCell>
              <TableCell>{subassembly.complete?<>complete</>:<>incomplete</>}</TableCell>
            </TableRow>
              {subassembly.components.map((component) => {
                return (
                  <TableRow
                  style={{ backgroundColor: "lavender"}}
                  >
                  <TableCell
                  style={{paddingLeft:80}}
                  ><MdSubdirectoryArrowRight/>{component.name}</TableCell>
                  <TableCell>{component.stock_level}</TableCell>
                  <TableCell>£{component.cost}</TableCell>
                  <TableCell>component</TableCell>
                  <TableCell></TableCell>
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
            <TableRow style={{ backgroundColor: "lightblue"}}>
              <TableCell style={{fontWeight:"bold"}}>Name</TableCell>
              <TableCell style={{fontWeight:"bold"}}>Stock Level</TableCell>
              <TableCell style={{fontWeight:"bold"}}>Cost</TableCell>
              <TableCell style={{fontWeight:"bold"}}>Category</TableCell>
              <TableCell style={{fontWeight:"bold"}}>Status</TableCell>
            </TableRow>
          </TableHead>
          
            {rows}
          
        </Table>
      </TableContainer>
    </>
  );
};

export default BOMTable;
