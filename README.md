---
page_type: sample
description: "A Python application that uses Azure Batch to process genomes in parallel with the SPAdes assembly tool."
languages:
- python
products:
- azure
---

# Batch Python File Processing with SPAdes

A Python application that uses Batch to process genomic files in parallel with the [SPAdes](http://cab.spbu.ru/software/spades/) assembly tool.
Original tutorial shows how to upload files into a container in a Storage account before processing them in Batch. This example assumes fastq.gz files are already available in a container.

## Prerequisites

- Azure Batch account and linked general-purpose Azure Storage account
- Python 2.7 or 3.3 or later including pip

## Instructions

- Clone repository
`git clone https://github.com/blue-moon22/azure-batch-python-example.git`
- Follow original tutorial [Run a parallel workload with Azure Batch using the Python API](https://docs.microsoft.com/azure/batch/tutorial-parallel-python).

## Resources

- [Azure Batch documentation](https://docs.microsoft.com/azure/batch/)
- [Azure Batch code samples](https://github.com/Azure/azure-batch-samples)

## Project code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
