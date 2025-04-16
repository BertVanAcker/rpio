+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Adaptation Manager       | AM-1  | Orchastrate adaptation process between components                    | Done  | N/A   | TB Simulator , TB4         | 0.3.0 |
+=================+==========================+=======+======================================================================+=======+=======+============================+=======+
| Architecture    | Communication Manager    | CM-1  | Communication between MAPLE-K component                              | Done  | N/A   | TB Simulator, TB4  , NTNU  | 0.3.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Design to Realization    | D2R-1 | Generate software component code skeleton from AADL                  | Done  | N/A   | TB Simulator               | 0.3.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Design to Realization    | D2R-2 | Generate costum messages from AADL                                   | Done  | N/A   | TB Simulator               | 0.3.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Knowledge Manager        | KM-1  | Use a local knowledge as shaerd knowledge between components         | Done  | N/A   | TB Simulator, TB4, NTNU    | 0.3.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Logging And Trancking    | L&T-1 | Use filesystem logger for logging the status of components           | Done  | N/A   | TB4  , TB Simulator, NTNU  | 0.3.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Logging And Trancking    | L&T-2 | Add a visualized Dashboard to show components activation status      | Done  | N/A   | TB4  , TB Simulator        | 0.3.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Concept to Design        | C2D-1 | Genarate AADL logical architecture from roboChart                    | Todo  | Done  | TB Simulator               | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Concept to Design        | C2D-2 | Generate standard AADL messages from roboChart                       | Todo  | Done  | TB Simulator               | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Communication Manager    | CM-2  | Use pub/sub protocol for communication manager (MQTT)                | Todo  | Done  | TB Simulator , TB4  , NTNU | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Design to Realization    | D2R-3 | Generate software component launch files from AADL                   | Todo  | Done  | TB Simulator               | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Design to Realization    | D2R-4 | Generate maple-k main file from AADL                                 | Todo  | Done  | TB Simulator               | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Design to Realization    | D2R-5 | Generate distributed deployment packege using docker                 | Todo  | Done  | TB Simulator               | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Transformations | Design to Realization    | D2R-6 | Create RPio package using command line interface                     | Todo  | Done  | TB Simulator               | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Knowledge Manager        | KM-2  | Use shared distrdibuted Knowledge in knowledge manager (Redis)       | Todo  | Done  | TB4  , NTNU, TB Simulator  | 0.3.3 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Adaptation Manager       | AM-2  | Seprate inter and intra component communication manager              | Todo  | Done  | TB Simulator               | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Adaptation Manager       | AM-3  | Add time-stamp to messgaes in communication and knowledge manager    | Todo  | Done  | TB Simulator               | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Adaptation Manager       | AM-4  | Add random uique-id in event messages                                | Todo  | Done  | TB Simulator               | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Communication Manager    | CM-3  | Support faster communication protocols_redis                         | Todo  | Done  | TB Simulator               | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Communication Manager    | CM-4  | Support faster communication protocols_rabbitMQ                      | Todo  | Done  | TB Simulator               | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Communication Manager    | CM-5  | Support faster communication protocols_UDP                           | Todo  | Done  | Not validated              | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Communication Manager    | CM-6  | Support faster communication protocols_TCP/IP                        | Todo  | Done  | Not validated              | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Knowledge Manager        | KM-3  | Support faster knowledge handing protocols_memcached                 | Todo  | Done  | TB Simulator               | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Knowledge Manager        | KM-4  | Support faster knowledge handing protocols_kafka                     | Todo  | Done  | Not validated              | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Knowledge Manager        | KM-5  | Support read/write knowledge using standard messages                 | Todo  | Done  | Not validated              | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Logging And Trancking    | L&T-3 | Support faster logging protocol in logging and tracking_redis        | Todo  | Done  | TB Simulator               | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Trustworthiness Checker  | TC-1  | Integrate first version of the trustworthiness checker (MQTT)        | Todo  | Done  | TB4  , TB Simulator        | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Trustworthiness Checker  | TC-2  | Support faster communication for the trustworthiness checker (MQTT)  | Todo  | Done  | TB4                        | 0.4.0 |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Communication Manager    | CM-7  | Support ROS2 for communication manager                               | Todo  | Todo  | Not validated              | Later |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Knowledge Manager        | KM-6  | Support LSTM model saving in knowledgebase                           | Todo  | Todo  | Not validated              | Later |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Knowledge Manager        | KM-7  | Support read/write hsitorical data in the knowledgebase              | Todo  | Todo  | Not validated              | Later |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+
| Architecture    | Logging And Trancking    | L&T-4 | Integrate the visualized dashboard in Logging and Tracking component | Todo  | Todo  | Not validated              | Later |
+-----------------+--------------------------+-------+----------------------------------------------------------------------+-------+-------+----------------------------+-------+