---
permalink: /about/
classes: wide
sidebar:
   - title: "ENCOPIA"
     text: "ENabling COnnected PrIvacy Assurance"
---

---

# About

---

## Project Goals 

We propose to use methods of binary analysis to make privacy goals testable in an automated fashion. ENCOPIA focuses on ensuring that sensitive data such as location information, user input, voice information, and other sensor readings can be tracked through programs and services by analyzing the used software and tracking data flows in programs. 

To achieve a holistic end-to-end evaluation of privacy critical data flows in IoT systems we strive to analyze the binaries deployed to IoT devices collecting most of the data as well as the byte code running as services in the cloud. Especially, actions will be taken combining the information from all analysis steps enabling the qualified assessment of sensitive information in the system’s sinks. 

Using information flow tracking, one can follow data that has been recorded at sources such as sensors to data sinks such as saved files or the network stack. Ideally, it is possible to track the information from an IoT device all the way into cloud databases, where the data is eventually used in further processing.


## Use Case IoT for e-Mobility 

The IoT for e-Mobility use case is based on the [ChargeAngels](http://www.chargeangels.fr/) application developed by SAP Labs France. ChargeAngels connects electric car charging stations, fleet administrators, cars and their drivers, and energy providers to monitor and analyze the usage of the charging stations and to optimize the balance between charging station workload, user experience, and operating costs. Its features include a monitoring dashboard, a mobile application for users including information about availability of charging stations and progress of charging, advanced analytical capacities, and APIs for external data processors like energy providers. 

The data collected and processed by the solution may include personal data like driver and vehicle ID, location information, charging profiles, and more. For example, before charging begins, the employee must present their company badge to the charging column. This contains the employee ID, which is sent to the cloud services and used to track energy usage per person. The technologies of the ENCOPIA project have the potential to improve and automate the compliance of the solution with data protection regulations like GDPR and detect and sanitize relevant data flows directly at the place where they are originating, thus, simplifying compliance. The ability to instrument code on the binary level is critical, since the components are provided by different vendors (e.g., the solution should allow to support charging stations of different vendors and different size) and access to the source code cannot always be assumed. ENCOPIA helps to support ChargeAngels scenarios with different privacy requirements, e.g., its usage for electric corporate fleets with company-owned cars and employees being the drivers, or its usage for public stations with private cars or drivers, by applying different policies to the detected data flows.
