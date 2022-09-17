rule _Nullsoft_Install_System_v1_98_wrrmpa
{
	meta:
		description = "Nullsoft Install System v1_98"
	strings:
		$a = {83EC0C535657FF152C8140}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
