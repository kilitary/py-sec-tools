rule _PKZIP_Archive_fdmvnk
{
	meta:
		description = "PKZIP Archive"
	strings:
		$a = {504B0304}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
