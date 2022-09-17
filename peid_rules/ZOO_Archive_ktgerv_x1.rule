rule _ZOO_Archive_ktgerv
{
	meta:
		description = "ZOO Archive"
	strings:
		$a = {5A4F4F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
