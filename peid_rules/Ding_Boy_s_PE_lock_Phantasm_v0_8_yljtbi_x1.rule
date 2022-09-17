rule _Ding_Boy_s_PE_lock_Phantasm_v0_8_yljtbi
{
	meta:
		description = "Ding Boy_s PE_lock Phantasm v0_8"
	strings:
		$a = {555756525153E8000000005D8BD581ED0D394000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
