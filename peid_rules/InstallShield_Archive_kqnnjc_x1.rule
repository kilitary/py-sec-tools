rule _InstallShield_Archive_kqnnjc
{
	meta:
		description = "InstallShield Archive"
	strings:
		$a = {2AAB79D8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
