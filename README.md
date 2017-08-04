# escholarship_data_parsing
This repository contains 2 scripts corresponding to the McGill eScholarship data.

One script is used to extract the metadata from the xml documents. You can modify the script to extract any specific metadata you want.

The second script is used to parse the filename and content of the html files. The script also cleans the data.

The output of both scripts is a list of dictionaries.

The output was dumped in Postgres tables and then the final dataset which contains the metadata and the html parsed text was exported to a csv file, which is publicly available for download at: 

For more information about the dataset, you can send an email to rajat.bhateja@mail.mcgill.ca
