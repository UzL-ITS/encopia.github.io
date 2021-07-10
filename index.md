---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: "ENCOPIA - ENabling COnnected PrIvacy Assurance"
layout: single
---

# Executive summary of the project 

Core concept and innovation: Today’s IoT devices collect huge amounts of data and share them with cloud services. In turn, Big Data analytics are used to analyze this data to provide new services such as predictive maintenance, more efficient routing and targeted advertisement. As the world becomes pervasively sentient with sensors placed in all kinds of daily devices, opting out is no longer possible. Devices like autonomous cars, smart screens and smart glasses will record personal information of all passersby, resulting in a conflict between individual privacy rights and the interest of making the benefits of big data analytics available to society as a whole. 

To ensure both goals are achievable, great care in the design and development of the complete IoT system from the device to the cloud service is necessary. This project aims at automating the verification of privacy goals of IoT services, from sensor devices all the way into the cloud services — during development and after deployment. 

Scientific and technological goals: We propose to use binary analysis methods to make privacy goals testable in an automated fashion for the complete life cycle of sensitive information. Tools developed in this project will ensure that sensitive data can be tracked through programs and services by analyzing the software used and tracking data flows within them. Automated privacy analysis tools do not exist today. Yet binary analysis has made great strides in the last years. With a combination of binary-level function detection and information flow tracking, data can be traced through applications along its life cycle, tracking its usage and detecting potential privacy breaches when they occur. By combining state-of-the-art binary analysis with dynamic data flow tracking in the cloud through JIT compiler instrumentation, we achieve an end-to-end privacy tracking of sensitive data.

Future outlook: The wide availability and sharing of vast amounts of data is necessary to drive digital innovation and leverage the powerful tools of big data and machine learning for the future knowledge society. The proposed tools will enable developers, third-party providers and users to ensure that data is used as intended and that protective mechanisms such as pseudonymization, encryption or differential privacy are applied. The researched methods can also be applied in certification schemes, which are currently under development under the European Cybersecurity Act. 

Synergy of collaboration: The consortium brings together partners from industry and academia with significant experience in building, operating and analyzing systems that handle private information. The companies include a startup specialized in automated binary analysis (Langlauf) and two big players in the European software market (SAP, Siemens), who represent a significant market share of IoT systems, from embedded systems solutions to cloud-based data processing. Together with the academic partners (EURECOM, University of Lübeck) we are able to represent the complete data life cycle of an IoT system and are equipped with the complementary knowledge required to build the described analysis components. 


# Context and objectives of the proposal 

## Objectives 

We propose to use methods of binary analysis to make privacy goals testable in an automated fashion. Encopia focuses on ensuring that sensitive data such as location information, user input, voice information, and other sensor readings can be tracked through programs and services by analyzing the used software and tracking data flows in programs. 

To achieve a holistic end-to-end evaluation of privacy critical data flows in IoT systems we strive to analyze the binaries deployed to IoT devices collecting most of the data as well as the byte code running as services in the cloud. Especially, actions will be taken combining the information from all analysis steps enabling the qualified assessment of sensitive information in the system’s sinks. 

Using information flow tracking, one can follow data that has been recorded at sources such as sensors to data sinks such as saved files or the network stack. Ideally, it is possible to track the information from an IoT device all the way into cloud databases, where the data is eventually used in further processing.


## Use Case IoT for e-Mobility 

The IoT for e-mobility use case is based on the ChargeAngels (http://www.chargeangels.fr/) application developed by SAP Labs France. ChargeAngels connects electric car charging stations, fleet administrators, cars and their drivers, and energy providers to monitor and analyze the usage of the charging stations and to optimize the balance between charging station workload, user experience, and operating costs. Its features include a monitoring dashboard, a mobile application for users including information about availability of charging stations and progress of charging, advanced analytical capacities, and APIs for external data processors like energy providers. 

The data collected and processed by the solution may include personal data like driver and vehicle ID, location information, charging profiles, and more. For example, before charging begins, the employee must present their company badge to the charging column. This contains the employee ID, which is sent to the cloud services and used to track energy usage per person. The technologies of the Encopia project have the potential to improve and automate the compliance of the solution with data protection regulations like GDPR and detect and sanitize relevant data flows directly at the place where they are originating, thus, simplifying compliance. The ability to instrument code on the binary level is critical, since the components are provided by different vendors (e.g., the solution should allow to support charging stations of different vendors and different size) and access to the source code cannot always be assumed. Encopia helps to support ChargeAngels scenarios with different privacy requirements, e.g., its usage for electric corporate fleets with company-owned cars and employees being the drivers, or its usage for public stations with private cars or drivers, by applying different policies to the detected data flows.
