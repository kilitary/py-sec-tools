rule _PLINK86_1984_1985_ierhch
{
	meta:
		description = "PLINK86 1984_ 1985"
	strings:
		$a = {FA8CC78CD68BCCBA????8EC226}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
