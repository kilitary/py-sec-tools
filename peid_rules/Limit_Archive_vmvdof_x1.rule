rule _Limit_Archive_vmvdof
{
	meta:
		description = "Limit Archive"
	strings:
		$a = {4C4D1A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
