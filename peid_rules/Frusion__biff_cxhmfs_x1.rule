rule _Frusion__biff_cxhmfs
{
	meta:
		description = "Frusion __ biff"
	strings:
		$a = {83EC0C535556576804010000C7442414}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
