rule _CrunchPE_gtlgnj
{
	meta:
		description = "CrunchPE"
	strings:
		$a = {55E8????????5D83ED068BC5556089AD????????2B85}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
