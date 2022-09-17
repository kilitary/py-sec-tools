rule _aPack_v0_98_m_marvzn
{
	meta:
		description = "aPack v0_98 _m"
	strings:
		$a = {1E068CC88ED805????8EC050BE????33FFFCB2??BD????33C950A4BB????3BF376}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
