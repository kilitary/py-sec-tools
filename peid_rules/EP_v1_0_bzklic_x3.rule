rule _EP_v1_0_bzklic
{
	meta:
		description = "EP v1_0"
	strings:
		$a = {81EB2A018B0F1E5B03CB0E51B9100151CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
