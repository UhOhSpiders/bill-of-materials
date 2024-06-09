valid_post="""{
  "name": "Advanced Gadget",
  "stock_level": 50,
  "subassemblies": [
    {
      "name": "Capacitor Bank",
      "complete": false,
      "cost": 75,
      "components": [
        {
          "name": "High-Capacity Capacitor",
          "stock_level": 10,
          "cost": 50
        },
        {
          "name": "Balancing Resistor",
          "stock_level": 25,
          "cost": 5
        },
        {
          "name": "Voltage Regulator",
          "stock_level": 5,
          "cost": 20
        }
      ]
    },
    {
      "name": "Sensor Module",
      "complete": true,
      "cost": 40,
      "components": [
        {
          "name": "Proximity Sensor",
          "stock_level": 15,
          "cost": 25
        },
        {
          "name": "Temperature Sensor",
          "stock_level": 20,
          "cost": 15
        }
      ]
    },
    {
      "name": "Microcontroller Unit (MCU)",
      "complete": true,
      "cost": 100,
      "components": [
        {
          "name": "Central Processing Unit (CPU)",
          "stock_level": 1,
          "cost": 70
        },
        {
          "name": "Memory Unit",
          "stock_level": 1,
          "cost": 20
        },
        {
          "name": "Input/Output (I/O) Controller",
          "stock_level": 1,
          "cost": 10
        }
      ]
    },
    {
      "name": "Wireless Module",
      "complete": false,
      "cost": 30,
      "components": [
        {
          "name": "Bluetooth Transceiver",
          "stock_level": 8,
          "cost": 20
        },
        {
          "name": "Antenna",
          "stock_level": 12,
          "cost": 10
        }
      ]
    }
  ]
}"""

modified_valid_post="""{
  "name": "Advanced Gizmo",
  "stock_level": 50,
  "subassemblies": [
    {
      "name": "Capacitor Bank",
      "complete": false,
      "cost": 75,
      "components": [
        {
          "name": "High-Capacity Capacitor",
          "stock_level": 10,
          "cost": 50
        },
        {
          "name": "Balancing Resistor",
          "stock_level": 25,
          "cost": 5
        },
        {
          "name": "Voltage Regulator",
          "stock_level": 5,
          "cost": 20
        }
      ]
    },
    {
      "name": "Sensor Module",
      "complete": true,
      "cost": 40,
      "components": [
        {
          "name": "Proximity Sensor",
          "stock_level": 15,
          "cost": 25
        },
        {
          "name": "Temperature Sensor",
          "stock_level": 20,
          "cost": 15
        }
      ]
    },
    {
      "name": "Microcontroller Unit (MCU)",
      "complete": true,
      "cost": 100,
      "components": [
        {
          "name": "Central Processing Unit (CPU)",
          "stock_level": 1,
          "cost": 70
        },
        {
          "name": "Memory Unit",
          "stock_level": 1,
          "cost": 20
        },
        {
          "name": "Input/Output (I/O) Controller",
          "stock_level": 1,
          "cost": 10
        }
      ]
    },
    {
      "name": "Wireless Module",
      "complete": false,
      "cost": 30,
      "components": [
        {
          "name": "Bluetooth Transceiver",
          "stock_level": 8,
          "cost": 20
        },
        {
          "name": "Antenna",
          "stock_level": 12,
          "cost": 10
        }
      ]
    }
  ]
}"""

invalid_post="""{
  "name": "Advanced Gadget",
  "stock_level": "fifty",
  "subassemblies": [
    {
      "name": "Capacitor Bank",
      "complete": false,
      "cost": 75,
      "components": [
        {
          "name": "High-Capacity Capacitor",
          "stock_level": 10,
          "cost": 50
        },
        {
          "name": "Balancing Resistor",
          "stock_level": 25,
          "cost": 5
        },
        {
          "name": "Voltage Regulator",
          "stock_level": 5,
          "cost": 20
        }
      ]
    },
    {
      "name": "Sensor Module",
      "complete": true,
      "cost": 40,
      "components": [
        {
          "name": "Proximity Sensor",
          "stock_level": 15,
          "cost": 25
        },
        {
          "name": "Temperature Sensor",
          "stock_level": 20,
          "cost": 15
        }
      ]
    },
    {
      "name": "Microcontroller Unit (MCU)",
      "complete": true,
      "cost": 100,
      "components": [
        {
          "name": "Central Processing Unit (CPU)",
          "stock_level": 1,
          "cost": 70
        },
        {
          "name": "Memory Unit",
          "stock_level": 1,
          "cost": 20
        },
        {
          "name": "Input/Output (I/O) Controller",
          "stock_level": 1,
          "cost": 10
        }
      ]
    },
    {
      "name": "Wireless Module",
      "complete": false,
      "cost": 30,
      "components": [
        {
          "name": "Bluetooth Transceiver",
          "stock_level": 8,
          "cost": 20
        },
        {
          "name": "Antenna",
          "stock_level": 12,
          "cost": 10
        }
      ]
    }
  ]
}"""