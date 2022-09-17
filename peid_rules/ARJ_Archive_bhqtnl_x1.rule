rule _ARJ_Archive_bhqtnl
{
	meta:
		description = "ARJ Archive"
	strings:
		$a = {60EA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
