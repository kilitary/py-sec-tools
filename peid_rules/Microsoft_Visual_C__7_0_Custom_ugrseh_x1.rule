rule _Microsoft_Visual_C__7_0_Custom_ugrseh
{
	meta:
		description = "Microsoft Visual C__ 7_0 Custom"
	strings:
		$a = {60BE00B044008DBE0060FBFF5783CDFFEB109090909090908A064688074701DB75078B1E83EEFC11DB72EDB80100000001DB75078B1E83EEFC11DB11C001DB73}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
