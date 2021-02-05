rule _Stony_Brook_Pascal_v6_14_wfuhwv
{
	meta:
		description = "Stony Brook Pascal v6_14"
	strings:
		$a = {31ED9A????????5589E5??EC????9A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
