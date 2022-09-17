rule _ASPack_v1_03b_wxyojm
{
	meta:
		description = "ASPack v1_03b"
	strings:
		$a = {60E8????????5D81EDAE9843??B8A89843??03C52B85189D43??8985249D43??80BD0E9D43}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
