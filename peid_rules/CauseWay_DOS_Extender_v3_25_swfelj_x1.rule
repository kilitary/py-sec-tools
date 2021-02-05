rule _CauseWay_DOS_Extender_v3_25_swfelj
{
	meta:
		description = "CauseWay DOS Extender v3_25"
	strings:
		$a = {FA161F26??????83????8ED0FB061607BE????8BFEB9????F3A407}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
