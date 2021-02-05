rule _Norton_Speed_Disk_Configuration_file_anpmfc
{
	meta:
		description = "Norton Speed Disk Configuration file"
	strings:
		$a = {4E6F72746F6E205370656564}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
