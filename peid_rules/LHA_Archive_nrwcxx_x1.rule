rule _LHA_Archive_nrwcxx
{
	meta:
		description = "LHA Archive"
	strings:
		$a = {??????6C6835}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
