rule _ASProtect_v1_23_RC1_jxyroa
{
	meta:
		description = "ASProtect v1_23 RC1"
	strings:
		$a = {5360BD????????8D45??8D5D??E8????????8D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
