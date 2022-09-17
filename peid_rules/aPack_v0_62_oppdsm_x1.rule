rule _aPack_v0_62_oppdsm
{
	meta:
		description = "aPack v0_62"
	strings:
		$a = {1E068CC88ED8??????8EC050BE????33FFFCB6}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
