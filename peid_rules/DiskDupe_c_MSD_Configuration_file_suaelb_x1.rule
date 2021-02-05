rule _DiskDupe_c_MSD_Configuration_file_suaelb
{
	meta:
		description = "DiskDupe _c_ MSD Configuration file"
	strings:
		$a = {4D534420446174612056657273}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
