rule _RatPacker_Glue_stub_yhwetr
{
	meta:
		description = "RatPacker _Glue_ stub"
	strings:
		$a = {4020FF00000000000000??BE006040008DBE00B0FFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
