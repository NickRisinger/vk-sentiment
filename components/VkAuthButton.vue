<script setup lang="ts">
import * as VKID from '@vkid/sdk';

onMounted(() => {
    VKID.Config.init({
        app: 53573521,
        redirectUrl: 'https://vk-sentiment.vercel.app/',
        responseMode: VKID.ConfigResponseMode.Callback,
        source: VKID.ConfigSource.LOWCODE,
        scope: '', // Заполните нужными доступами по необходимости
    });

    const oneTap = new VKID.OneTap();

    oneTap.render({
        container: document.querySelector('#auth-ntn')!,
        showAlternativeLogin: true,
        styles: {
            borderRadius: 16
        }
    })
        .on(VKID.WidgetEvents.ERROR, vkidOnError)
        .on(VKID.OneTapInternalEvents.LOGIN_SUCCESS, function (payload: any) {
            console.log('TEST payload:', payload);
            const code = payload.code;
            const deviceId = payload.device_id;

            VKID.Auth.exchangeCode(code, deviceId)
                .then(vkidOnSuccess)
                .catch(vkidOnError);
        });

    function vkidOnSuccess(data: any) {
        // Обработка полученного результата
        console.log('vkidOnSuccess:', data);
    }

    function vkidOnError(error: any) {
        // Обработка ошибки
        console.log('vkidOnError:', error);
    }
})
</script>

<template>
    <div id="auth-ntn"></div>
</template>

<style scoped>

</style>
