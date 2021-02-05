rule _ARJ_SFX_Custom_qwnpic
{
	meta:
		description = "ARJ SFX Custom"
	strings:
		$a = {B8????????669C60508D905C0100006800004000833A000F84C6C1FFFF8B04248B0A0FBAF11F7313FD8BF08BF8037204037A08F3A583C20CFCEBD983C2108B5A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
