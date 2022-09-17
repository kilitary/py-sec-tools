rule _RTPatch_software_update_package_data_file_gfdjwo
{
	meta:
		description = "RTPatch software update package data file"
	strings:
		$a = {4B2A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
