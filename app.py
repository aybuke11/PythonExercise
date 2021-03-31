import json

data = '''
{
  "ApplicationName": {
    "S": "Rebate"
  },
  "Bookings": {
    "L": [
      {
        "M": {
          "IsEmpty": {
            "N": "0"
          },
          "IsProcessed": {
            "N": "1"
          },
          "Lines": {
            "L": [
              {
                "M": {
                  "Baf": {
                    "N": "202"
                  },
                  "Sf": {
                    "N": "0"
                  }
                }
              }
            ]
          },
          "ProcessedAmount": {
            "N": "202"
          },
          "ReleaseNumber": {
            "S": "49142949"
          },
          "TotalAmount": {
            "N": "202"
          },
          "UnitNumber": {
            "S": "31AYU03"
          },
          "UnitType": {
            "S": "T/T"
          },
          "VehicleRegNumber": {
            "S": "31BD454"
          }
        }
      }
    ]
  },
  "Customer": {
    "M": {
      "Address": {
        "SS": [
          "CEKMECE MAHALLESI ATATURK CADDESI N"
        ]
      },
      "City": {
        "S": "HATAY"
      },
      "Country": {
        "S": "TURKEY"
      },
      "County": {
        "S": "DEFNE"
      },
      "IsOctet": {
        "N": "0"
      },
      "Name": {
        "S": "GÜNSALDI GÜBRE PAZ. GIDA TIC.TAS.LTD.STI"
      },
      "Number": {
        "S": "88611"
      },
      "Phone": {
        "S": "903262253906"
      },
      "PostCode": {
        "S": "31060"
      }
    }
  },
  "InvoiceDate": {
    "N": "1580342400"
  },
  "InvoiceId": {
    "S": "400000892"
  },
  "LineType": {
    "N": "0"
  },
  "PaymentMethod": {
    "N": "1"
  },
  "ProcessedAmount": {
    "N": "202"
  },
  "ScheduleDate": {
    "N": "1579892400"
  },
  "Source": {
    "S": "PHX"
  },
  "SourceInvoiceId": {
    "S": "PHX-400000892"
  },
  "TotalAmount": {
    "N": "202"
  },
  "VesselCode": {
    "S": "UGLT"
  },
  "VesselName": {
    "S": "Cemil Bayulgen"
  },
  "VoyageNumber": {
    "S": "SETYAL024120"
  }
}
'''

j = json.loads(data)
from pprint import pprint
pprint.pprint(j)

for key in j:
    for attr, val in key.iteritems():
        pprint(key)
        pprint(attr)
        pprint(val)