rule _HPACK_Archive_ewqicu
{
	meta:
		description = "HPACK Archive"
	strings:
		$a = {4850414B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
