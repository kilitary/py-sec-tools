rule _modified_HACKSTOP_v1_11f_noubvf
{
	meta:
		description = "modified HACKSTOP v1_11f"
	strings:
		$a = {52B430CD2152FA??FB3D????EB??CD200E1FB409E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
