rule _Ding_Boy_s_PE_lock_v0_07_ipqhfz
{
	meta:
		description = "Ding Boy_s PE_lock v0_07"
	strings:
		$a = {555756525153E8000000005D8BD581ED23354000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
