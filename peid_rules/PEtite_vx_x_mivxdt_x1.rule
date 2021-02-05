rule _PEtite_vx_x_mivxdt
{
	meta:
		description = "PEtite vx_x"
	strings:
		$a = {B8????????669C6050}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
