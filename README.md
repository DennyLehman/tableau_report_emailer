"# This project pulls a tableau view from tableau online and emails the report out to a group of users." 
# Tableau report Emailer

This project demonstrates how to build a cash flow model using python data tools as an alternative to an excel based model. Dummy systems are setup with recurring payments, escalators, inservice dates, and various other initial conditions. A pandas dataframe is used to store the dates and cash flows of each system. A date range with the minimum starting inservice date through the maximum end date is constructed and used as the dataframe index. Each system name is stored as a column in the dateframe and cash flows are calculated based on the equation:
cash_flow = recurring payment * (1 + escalator) ^ (number of years since inservice)
Each system's cash flow is added to a cumulative sum for a npv calculation on the entire fleet. The project outputs the npv of the fleet.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Prerequisites for this project include python 3.X with installed packages for data analytics.
What things you need to install the software and how to install them

```
pandas 0.20.2
numpy 1.12.1
datetime
cfprocess
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Denny Lehman** - *Initial work* - [DennyLehman](https://github.com/DennyLehman)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
"# Cashflow_fleet_level_framework" 
