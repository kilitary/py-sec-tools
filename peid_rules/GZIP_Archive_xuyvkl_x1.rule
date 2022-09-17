rule _GZIP_Archive_xuyvkl
{
	meta:
		description = "GZIP Archive"
	strings:
		$a = {1F8B0808??????35}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
