rule _The_Norton_Antivirus_Information_file_xlqvxd
{
	meta:
		description = "The Norton Antivirus Information file"
	strings:
		$a = {546865204E6F72746F6E20416E7469566972757320496E666F726D6174696F6E2046696C65}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
