rule _aPack_v0_98b_com__jfxjbo
{
	meta:
		description = "aPack v0_98b _com_"
	strings:
		$a = {BE????BF????8BCFFC57F3A4C3BF????5757BE????B2??BD????50A4}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
