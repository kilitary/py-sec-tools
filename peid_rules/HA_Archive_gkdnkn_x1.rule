rule _HA_Archive_gkdnkn
{
	meta:
		description = "HA Archive"
	strings:
		$a = {4841}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
